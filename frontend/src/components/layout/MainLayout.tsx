import { ReactNode, useEffect, useState } from 'react';
import { Navbar } from './Navbar';
import { Sidebar } from './Sidebar';
import { getInitialTheme, storageKey } from '../../lib/theme';
import { Toast } from '../ui/Toast';

interface MainLayoutProps {
  children: ReactNode;
}

export function MainLayout({ children }: MainLayoutProps) {
  const [theme, setTheme] = useState<'light' | 'dark'>(getInitialTheme);
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [toast, setToast] = useState<{ title: string; description?: string } | null>(null);

  useEffect(() => {
    document.documentElement.classList.toggle('dark', theme === 'dark');
    window.localStorage.setItem(storageKey, theme);
  }, [theme]);

  useEffect(() => {
    setToast({ title: 'Welcome to StockVision', description: 'AI-driven insights are ready for you.' });
  }, []);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 transition-colors dark:bg-slate-950 dark:text-slate-100">
      <Navbar theme={theme} onToggleTheme={() => setTheme(theme === 'dark' ? 'light' : 'dark')} onToggleSidebar={() => setSidebarOpen((value) => !value)} />
      <div className="mx-auto flex max-w-7xl gap-6 px-4 py-6 sm:px-6 lg:px-8">
        <Sidebar open={sidebarOpen} />
        <main className="flex-1 lg:pl-0">{children}</main>
      </div>
      <div className="fixed bottom-4 right-4 z-40 w-80">
        {toast ? <Toast title={toast.title} description={toast.description} onClose={() => setToast(null)} /> : null}
      </div>
    </div>
  );
}
