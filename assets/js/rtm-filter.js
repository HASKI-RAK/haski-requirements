(function(){
  function ready(fn){ if(document.readyState !== 'loading'){ fn(); } else { document.addEventListener('DOMContentLoaded', fn); } }
  ready(function(){
    const searchInput = document.getElementById('rtm-search');
    const statusSelect = document.getElementById('rtm-status-filter');
    const table = document.getElementById('rtm-table');
    if(!table) return;
    const rows = Array.from(table.querySelectorAll('tbody tr'));

    function normalize(v){ return (v||'').toLowerCase(); }

    function apply(){
      const q = normalize(searchInput && searchInput.value);
      const st = statusSelect ? statusSelect.value : '';
      rows.forEach(tr => {
        const text = normalize(tr.textContent);
        const rowStatus = tr.getAttribute('data-status') || '';
        let ok = true;
        if(q && !text.includes(q)) ok = false;
        if(st && rowStatus !== st) ok = false;
        if(ok) tr.removeAttribute('hidden'); else tr.setAttribute('hidden','');
      });
    }

    if(searchInput) searchInput.addEventListener('input', apply);
    if(statusSelect) statusSelect.addEventListener('change', apply);
    apply();
  });
})();
