// localStorage with a safe fallback (private mode, blocked storage). Values are JSON, as in the prototype.
export const store = {
  get<T = any>(k: string, d: T): T { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch { return d; } },
  set(k: string, v: unknown) { try { localStorage.setItem(k, JSON.stringify(v)); } catch { /* ignore */ } },
};
