/**
 * AppGuard: Production reliability and state completeness runtime
 * Adapted from DesignMotionHQ UX Engine architecture.
 *
 * Ensures a user is never left on a blank, dead, or unhandled screen.
 * Load this script first in <head> before other application scripts.
 */
(function() {
  'use strict';

  var isReady = false;
  var bootTimer = null;
  var BOOT_TIMEOUT_MS = 6000;

  var AppGuard = {
    init: function() {
      // 1. Boot Guard: Set timeout for application load
      bootTimer = setTimeout(function() {
        if (!isReady) {
          AppGuard.fail('boot', 'Application failed to initialize within expected window.');
        }
      }, BOOT_TIMEOUT_MS);

      // 2. Unhandled Errors
      window.addEventListener('error', function(event) {
        console.error('[AppGuard Uncaught Error]', event.error || event.message);
        AppGuard.fail('runtime', event.message || 'An unexpected error occurred.');
      });

      window.addEventListener('unhandledrejection', function(event) {
        console.error('[AppGuard Unhandled Rejection]', event.reason);
        var msg = (event.reason && (event.reason.message || event.reason.toString())) || 'Unhandled promise rejection';
        AppGuard.fail('network', msg);
      });

      // 3. Offline / Online Connectivity Banner
      window.addEventListener('offline', function() {
        AppGuard.showOfflineBanner(true);
      });
      window.addEventListener('online', function() {
        AppGuard.showOfflineBanner(false);
      });
      if (!navigator.onLine) {
        AppGuard.showOfflineBanner(true);
      }

      // 4. Double Submit Guard on forms & action buttons
      document.addEventListener('submit', function(e) {
        var form = e.target;
        if (form.getAttribute('data-guard-submitting') === 'true') {
          e.preventDefault();
          return false;
        }
        form.setAttribute('data-guard-submitting', 'true');
        var submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.setAttribute('data-original-text', submitBtn.innerText || submitBtn.value);
          if (submitBtn.tagName === 'BUTTON') {
            submitBtn.innerHTML = '<span class="ag-spinner"></span> Processing...';
          }
        }
        setTimeout(function() {
          form.removeAttribute('data-guard-submitting');
          if (submitBtn) {
            submitBtn.disabled = false;
            if (submitBtn.getAttribute('data-original-text')) {
              submitBtn.innerText = submitBtn.getAttribute('data-original-text');
            }
          }
        }, 8000);
      }, true);
    },

    ready: function() {
      isReady = true;
      if (bootTimer) {
        clearTimeout(bootTimer);
        bootTimer = null;
      }
      var bootEl = document.getElementById('ag-error-panel');
      if (bootEl) {
        bootEl.remove();
      }
    },

    fail: function(type, message) {
      if (document.getElementById('ag-error-panel')) return;

      var panel = document.createElement('div');
      panel.id = 'ag-error-panel';
      panel.style.cssText = [
        'position: fixed',
        'inset: 0',
        'z-index: 999999',
        'background: #0B0F17',
        'color: #F1F5F9',
        'display: flex',
        'align-items: center',
        'justify-content: center',
        'font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        'padding: 24px',
        'box-sizing: border-box'
      ].join(';');

      var card = document.createElement('div');
      card.style.cssText = [
        'background: #151D2A',
        'border: 1px solid #233147',
        'border-radius: 12px',
        'max-width: 460px',
        'width: 100%',
        'padding: 32px',
        'box-shadow: 0 20px 40px rgba(0,0,0,0.5)',
        'text-align: left'
      ].join(';');

      var title = type === 'boot' ? 'Application Load Interrupted' : 'Something Went Wrong';
      var desc = message || 'The interface encountered an unexpected state. Your data is safe.';

      card.innerHTML = [
        '<div style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">',
        '  <div style="width:36px;height:36px;border-radius:8px;background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);display:flex;align-items:center;justify-content:center;color:#EF4444;font-weight:bold;">!</div>',
        '  <h2 style="margin:0;font-size:18px;font-weight:600;color:#F8FAFC;">' + title + '</h2>',
        '</div>',
        '<p style="margin:0 0 24px 0;font-size:14px;line-height:1.6;color:#94A3B8;">' + desc + '</p>',
        '<div style="display:flex;gap:12px;">',
        '  <button id="ag-reload-btn" style="flex:1;background:#2563EB;color:#fff;border:none;border-radius:6px;padding:10px 16px;font-size:14px;font-weight:500;cursor:pointer;">Reload Application</button>',
        '  <button id="ag-home-btn" style="background:#1E293B;color:#CBD5E1;border:1px solid #334155;border-radius:6px;padding:10px 16px;font-size:14px;cursor:pointer;">Return Home</button>',
        '</div>'
      ].join('');

      panel.appendChild(card);
      document.body.appendChild(panel);

      document.getElementById('ag-reload-btn').addEventListener('click', function() {
        window.location.reload(true);
      });
      document.getElementById('ag-home-btn').addEventListener('click', function() {
        window.location.href = '/';
      });
    },

    showOfflineBanner: function(show) {
      var banner = document.getElementById('ag-offline-banner');
      if (show) {
        if (!banner) {
          banner = document.createElement('div');
          banner.id = 'ag-offline-banner';
          banner.style.cssText = [
            'position: fixed',
            'top: 0',
            'left: 0',
            'right: 0',
            'z-index: 999990',
            'background: #D97706',
            'color: #FFFFFF',
            'font-family: -apple-system, sans-serif',
            'font-size: 13px',
            'font-weight: 500',
            'text-align: center',
            'padding: 8px 16px',
            'box-shadow: 0 2px 8px rgba(0,0,0,0.2)'
          ].join(';');
          banner.innerText = 'You are currently offline. Changes are saved locally and will sync when reconnected.';
          document.body.appendChild(banner);
        }
      } else {
        if (banner) {
          banner.remove();
        }
      }
    }
  };

  // Auto initialize on DOM ready or immediate if head exists
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', AppGuard.init);
  } else {
    AppGuard.init();
  }

  window.AppGuard = AppGuard;
})();
