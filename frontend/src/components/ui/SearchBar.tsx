import { Search } from 'lucide-react';

interface SearchBarProps {
  placeholder?: string;
  value?: string;
  onChange?: (value: string) => void;
}

export function SearchBar({ placeholder = 'Search stocks...', value = '', onChange }: SearchBarProps) {
  return (
    <label className="flex items-center gap-3 rounded-full border border-slate-200 bg-white px-4 py-3 text-sm text-slate-500 shadow-sm dark:border-slate-800 dark:bg-slate-900 dark:text-slate-400">
      <Search className="h-4 w-4" />
      <input
        value={value}
        onChange={(event) => onChange?.(event.target.value)}
        className="w-full bg-transparent outline-none"
        placeholder={placeholder}
      />
    </label>
  );
}
