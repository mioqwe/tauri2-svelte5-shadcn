// place files you want to import through the `$lib` alias in this folder.
export * from './commands.svelte';
import { fetch } from '@tauri-apps/plugin-http';
import { PUBLIC_API_URL } from '$env/static/public';

export async function ftch(
  url: string, 
  method: string = 'GET', 
  params: RequestInit = {}
) {
  const fullUrl = `${PUBLIC_API_URL}${url}`;
  const options: RequestInit = {
    method,
    headers: {
      'Content-Type': 'application/json',
      ...(params.headers || {})
    },
    ...params
  };

  // If there's a body and it's not already a string, convert it to JSON.
  if (options.body && typeof options.body !== 'string') {
    options.body = JSON.stringify(options.body);
  }

  return fetch(fullUrl, options).then(response => response.text());
}