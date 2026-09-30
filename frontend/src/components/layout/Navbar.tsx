import { Moon, SunMedium, Bell, Menu } from 'lucide-react';
import { NavLink } from 'react-router-dom';
import { Button } from '../ui/Button';

interface NavbarProps {
  theme: 'light' | 'dark';
  onToggleTheme: () => void;
  onToggleSidebar: () => void;
}

export function Navbar({ theme, onToggleTheme, onToggleSidebar }: NavbarProps) {
  return (
    <header className="sticky top-0 z-20 border-b border-slate-200/70 bg-white/80 backdrop-blur dark:border-slate-800 dark:bg-slate-950/80">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
        <div className="flex items-center gap-3">
          <button onClick={onToggleSidebar} className="rounded-full p-2 text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800 lg:hidden">
            <Menu className="h-5 w-5" />
          </button>
          <div>
            <p className="text-lg font-semibold text-slate-900 dark:text-white">STOCK VISION</p>
            <p className="text-xs text-slate-500 dark:text-slate-400">AI Stock Intelligence</p>
          </div>
        </div>

        <nav className="hidden items-center gap-2 md:flex">
          {[
            ['/', 'Home'],
            ['/dashboard', 'Dashboard'],
            ['/analysis', 'Analysis'],
            ['/prediction', 'Prediction'],
            ['/news', 'News']
          ].map(([to, label]) => (
            <NavLink key={to} to={to} className={({ isActive }) => `rounded-full px-3 py-2 text-sm transition ${isActive ? 'bg-blue-600 text-white' : 'text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800'}`}>
              {label}
            </NavLink>
          ))}
        </nav>

        <div className="flex items-center gap-2">
          <button onClick={onToggleTheme} className="rounded-full p-2 text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800">
            {theme === 'dark' ? <SunMedium className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
          </button>
          <button className="rounded-full p-2 text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800">
            <Bell className="h-5 w-5" />
          </button>
          <Button variant="primary">Sign In</Button>
        </div>
      </div>
    </header>
  );
}
