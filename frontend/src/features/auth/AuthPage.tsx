import { useState } from 'react';
import { Card } from '../../components/ui/Card';
import { Button } from '../../components/ui/Button';

export function AuthPage() {
  const [mode, setMode] = useState<'login' | 'register' | 'forgot'>('login');

  return (
    <div className="mx-auto flex max-w-5xl items-center justify-center py-10">
      <Card className="w-full max-w-md space-y-6">
        <div className="space-y-2">
          <h1 className="text-2xl font-semibold text-slate-900 dark:text-white">{mode === 'login' ? 'Welcome back' : mode === 'register' ? 'Create account' : 'Reset password'}</h1>
          <p className="text-sm text-slate-500 dark:text-slate-400">Secure access to your AI market workspace.</p>
        </div>
        <div className="flex rounded-full bg-slate-100 p-1 dark:bg-slate-800">
          {['login', 'register', 'forgot'].map((option) => (
            <button key={option} onClick={() => setMode(option as 'login' | 'register' | 'forgot')} className={`flex-1 rounded-full px-3 py-2 text-sm ${mode === option ? 'bg-blue-600 text-white' : 'text-slate-600 dark:text-slate-300'}`}>
              {option === 'login' ? 'Login' : option === 'register' ? 'Register' : 'Forgot'}
            </button>
          ))}
        </div>
        <div className="space-y-3">
          {mode !== 'forgot' ? <input className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="Email" /> : null}
          {mode !== 'forgot' ? <input className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="Password" type="password" /> : null}
          {mode === 'register' ? <input className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="Confirm password" type="password" /> : null}
          {mode === 'forgot' ? <input className="w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 dark:border-slate-800 dark:bg-slate-900" placeholder="Email" /> : null}
          <Button variant="primary" className="w-full">{mode === 'login' ? 'Sign in' : mode === 'register' ? 'Create account' : 'Send reset link'}</Button>
        </div>
      </Card>
    </div>
  );
}
