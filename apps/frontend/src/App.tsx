import { useEffect, useState } from 'react';

type HealthResponse = {
  status: string;
  service: string;
};

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000';

export function App() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchHealth = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (!response.ok) {
          throw new Error(`Healthcheck failed with status ${response.status}`);
        }
        const data = (await response.json()) as HealthResponse;
        setHealth(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unexpected error');
      }
    };

    void fetchHealth();
  }, []);

  return (
    <main className="mx-auto flex min-h-screen max-w-3xl flex-col items-center justify-center gap-4 p-8 text-center">
      <h1 className="text-5xl font-bold text-emerald-400">TeachLead</h1>
      <p className="text-slate-300">Monorepo base com FastAPI + React + Docker.</p>

      {health ? (
        <div className="rounded border border-emerald-500/30 bg-emerald-500/10 p-4 text-emerald-300">
          Backend: {health.service} ({health.status})
        </div>
      ) : error ? (
        <div className="rounded border border-rose-500/30 bg-rose-500/10 p-4 text-rose-300">Erro: {error}</div>
      ) : (
        <div className="rounded border border-slate-700 bg-slate-800 p-4 text-slate-300">Verificando /health...</div>
      )}
    </main>
  );
}
