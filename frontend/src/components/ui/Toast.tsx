import { useEffect } from 'react';

interface ToastProps {
  title: string;
  description?: string;
  onClose: () => void;
}

export function Toast({ title, description, onClose }: ToastProps) {
  useEffect(() => {
    const timer = window.setTimeout(onClose, 2500);
    return () => window.clearTimeout(timer);
  }, [onClose]);

  return (
    <div className="rounded-2xl border border-slate-200 bg-white/95 p-4 shadow-xl backdrop-blur dark:border-slate-800 dark:bg-slate-900/95">
      <div className="font-medium text-slate-900 dark:text-white">{title}</div>
      {description ? <div className="mt-1 text-sm text-slate-500 dark:text-slate-400">{description}</div> : null}
    </div>
  );
}
