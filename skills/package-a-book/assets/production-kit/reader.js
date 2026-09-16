/* Local-only reading progress. Account sync requires an authenticated backend. */
(() => {
  const root = document.documentElement;
  const key = root.dataset.bookStorageKey;
  const progress = document.querySelector('[data-reading-progress]');
  const timeLeft = document.querySelector('[data-reading-time-left]');
  const content = document.querySelector('[data-book-content]') || document.querySelector('main');
  const selectionTools = document.querySelector('[data-selection-toolbar]');
  if (!key || !progress || !content) return;

  const clamp = (value) => Math.max(0, Math.min(1, value));
  const restore = () => {
    const saved = Number(localStorage.getItem(`${key}:progress`));
    if (!Number.isFinite(saved) || saved <= 0) return false;
    requestAnimationFrame(() => {
      scrollTo(0, saved * (document.body.scrollHeight - innerHeight));
      requestAnimationFrame(save);
    });
    return true;
  };
  const save = () => {
    const length = document.body.scrollHeight - innerHeight;
    const value = length > 0 ? clamp(scrollY / length) : 1;
    progress.value = value;
    progress.setAttribute('aria-valuenow', String(Math.round(value * 100)));
    if (timeLeft) {
      const words = content.textContent.trim().split(/\s+/).filter(Boolean).length;
      const minutes = Math.max(0, Math.ceil((words * (1 - value)) / 200));
      timeLeft.textContent = minutes ? `About ${minutes} min left` : 'Finished';
    }
    localStorage.setItem(`${key}:progress`, String(value));
  };

  const hideSelectionTools = () => {
    if (!selectionTools) return;
    selectionTools.hidden = true;
    selectionTools.setAttribute('aria-hidden', 'true');
  };
  const updateSelectionTools = () => {
    if (!selectionTools) return;
    const selection = getSelection();
    const range = selection && selection.rangeCount ? selection.getRangeAt(0) : null;
    const selectedInsideBook = range && !range.collapsed && selection.toString().trim() && content.contains(range.commonAncestorContainer);
    selectionTools.hidden = !selectedInsideBook;
    selectionTools.setAttribute('aria-hidden', String(!selectedInsideBook));
  };

  addEventListener('load', () => { if (!restore()) save(); }, { once: true });
  addEventListener('scroll', save, { passive: true });
  addEventListener('resize', save, { passive: true });
  document.addEventListener('selectionchange', updateSelectionTools);
  document.addEventListener('pointerdown', (event) => {
    if (selectionTools && !selectionTools.hidden && !selectionTools.contains(event.target)) {
      hideSelectionTools();
      getSelection()?.removeAllRanges();
    }
  });
})();
