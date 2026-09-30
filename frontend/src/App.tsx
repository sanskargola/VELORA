import { Routes, Route } from 'react-router-dom';
import { MainLayout } from './components/layout/MainLayout';
import { LandingPage } from './features/landing/LandingPage';
import { AuthPage } from './features/auth/AuthPage';
import { DashboardPage } from './features/dashboard/DashboardPage';
import { AnalysisPage } from './features/analysis/AnalysisPage';
import { PredictionPage } from './features/prediction/PredictionPage';
import { PortfolioPage } from './features/portfolio/PortfolioPage';
import { WatchlistPage } from './features/watchlist/WatchlistPage';
import { NewsPage } from './features/news/NewsPage';
import { ProfilePage } from './features/profile/ProfilePage';
import { AdminPage } from './features/admin/AdminPage';

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<MainLayout><LandingPage /></MainLayout>} />
      <Route path="/auth" element={<MainLayout><AuthPage /></MainLayout>} />
      <Route path="/dashboard" element={<MainLayout><DashboardPage /></MainLayout>} />
      <Route path="/analysis" element={<MainLayout><AnalysisPage /></MainLayout>} />
      <Route path="/prediction" element={<MainLayout><PredictionPage /></MainLayout>} />
      <Route path="/portfolio" element={<MainLayout><PortfolioPage /></MainLayout>} />
      <Route path="/watchlist" element={<MainLayout><WatchlistPage /></MainLayout>} />
      <Route path="/news" element={<MainLayout><NewsPage /></MainLayout>} />
      <Route path="/profile" element={<MainLayout><ProfilePage /></MainLayout>} />
      <Route path="/admin" element={<MainLayout><AdminPage /></MainLayout>} />
    </Routes>
  );
}
