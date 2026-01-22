'use client';

import { useState, FormEvent, ChangeEvent } from 'react';

interface Response {
  prompt: string;
  generated_text: string;
  full_text: string;
}

export default function Home() {
  const [prompt, setPrompt] = useState<string>('');
  const [response, setResponse] = useState<Response | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string>('');
  const [maxLength, setMaxLength] = useState<number>(20);
  const [temperature, setTemperature] = useState<number>(0.7);

  const handleGenerate = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    
    if (!prompt.trim()) {
      setError('Please enter a prompt');
      return;
    }

    setLoading(true);
    setError('');
    setResponse(null);

    try {
      const backendUrl: string = typeof window !== 'undefined' 
        ? (process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000')
        : 'http://localhost:8000';
        
      const res = await fetch(`${backendUrl}/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt,
          max_length: maxLength,
          temperature,
        }),
      });

      if (!res.ok) throw new Error(`API error: ${res.status}`);
      const data = await res.json();
      setResponse(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to generate text');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex items-center justify-center p-4">
      <div className="max-w-2xl w-full">
        <div className="bg-white rounded-lg shadow-2xl p-8">
          {/* Header */}
          <div className="mb-8">
            <h1 className="text-4xl font-bold text-gray-800 mb-2">
              Simple LLM Generator
            </h1>
            <p className="text-gray-600">
              Enter a prompt and let the model complete your text
            </p>
          </div>

          {/* Form */}
          <form onSubmit={handleGenerate} className="space-y-6">
            {/* Prompt Input */}
            <div>
              <label htmlFor="prompt" className="block text-sm font-medium text-gray-700 mb-2">
                Prompt
              </label>
              <textarea
                id="prompt"
                value={prompt}
                onChange={(e: ChangeEvent<HTMLTextAreaElement>) => setPrompt(e.target.value)}
                placeholder="e.g., The cat sat on..."
                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent resize-none"
                rows={3}
                disabled={loading}
              />
            </div>

            {/* Controls */}
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label htmlFor="maxLength" className="block text-sm font-medium text-gray-700 mb-2">
                  Max Length: {maxLength}
                </label>
                <input
                  id="maxLength"
                  type="range"
                  min="5"
                  max="50"
                  value={maxLength}
                  onChange={(e: ChangeEvent<HTMLInputElement>) => setMaxLength(Number(e.target.value))}
                  className="w-full"
                  disabled={loading}
                />
              </div>

              <div>
                <label htmlFor="temperature" className="block text-sm font-medium text-gray-700 mb-2">
                  Temperature: {temperature.toFixed(1)}
                </label>
                <input
                  id="temperature"
                  type="range"
                  min="0.1"
                  max="2"
                  step="0.1"
                  value={temperature}
                  onChange={(e: ChangeEvent<HTMLInputElement>) => setTemperature(Number(e.target.value))}
                  className="w-full"
                  disabled={loading}
                />
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-indigo-600 hover:bg-indigo-700 disabled:bg-gray-400 text-white font-bold py-3 rounded-lg transition"
            >
              {loading ? 'Generating...' : 'Generate Text'}
            </button>
          </form>

          {/* Error Message */}
          {error && (
            <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-red-700 font-medium">Error: {error}</p>
            </div>
          )}

          {/* Response */}
          {response && (
            <div className="mt-8 space-y-4">
              <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <h3 className="font-semibold text-gray-800 mb-2">Prompt:</h3>
                <p className="text-gray-700">{response.prompt}</p>
              </div>

              <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                <h3 className="font-semibold text-gray-800 mb-2">Generated Text:</h3>
                <p className="text-gray-700">{response.generated_text}</p>
              </div>

              <div className="p-4 bg-purple-50 border border-purple-200 rounded-lg">
                <h3 className="font-semibold text-gray-800 mb-2">Full Output:</h3>
                <p className="text-gray-700">{response.full_text}</p>
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="text-center mt-6 text-gray-600 text-sm">
          <p>Built with PyTorch, FastAPI, and Next.js</p>
        </div>
      </div>
    </main>
  );
}
