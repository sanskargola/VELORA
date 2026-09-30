import { LayoutDashboard, BarChart3, TrendingUp, Newspaper, Wallet, Shield, UserCircle } from 'lucide-react';
import { NavLink } from 'react-router-dom';

const items = [
  { to: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { to: '/analysis', label: 'Analysis', icon: BarChart3 },
  { to: '/prediction', label: 'Prediction', icon: TrendingUp },
  { to: '/portfolio', label: 'Portfolio', icon: Wallet },
  { to: '/watchlist', label: 'Watchlist', icon: BarChart3 },
  { to: '/news', label: 'News', icon: Newspaper },
  { to: '/profile', label: 'Profile', icon: UserCircle },
  { to: '/admin', label: 'Admin', icon: Shield },
];

interface SidebarProps {
  open: boolean;
}

export function Sidebar({ open }: SidebarProps) {
  return (
    <aside className={`fixed inset-y-0 left-0 z-30 w-72 border-r border-slate-200/70 bg-white/90 p-5 backdrop-blur transition-transform dark:border-slate-800 dark:bg-slate-950/90 lg:sticky lg:top-16 lg:h-[calc(100vh-4rem)] lg:translate-x-0 ${open ? 'translate-x-0' : '-translate-x-full'}`}>
      <div className="space-y-2">
        {items.map(({ to, label, icon: Icon }) => (
          <NavLink key={to} to={to} className={({ isActive }) => `flex items-center gap-3 rounded-2xl px-3 py-3 text-sm transition ${isActive ? 'bg-blue-600 text-white' : 'text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800'}`}>
            <Icon className="h-4 w-4" />
            {label}
          </NavLink>
        ))}
      </div>
    </aside>
  );
}
