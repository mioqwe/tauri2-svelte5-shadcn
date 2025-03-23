<script>
	import Aside from '$lib/comps/aside.svelte';
	import { ftch } from '$lib';
	import Terminal from '$lib/comps/Terminal.svelte';
	import { onMount } from 'svelte';
	import { register, isRegistered, unregisterAll } from '@tauri-apps/plugin-global-shortcut';
	let { children } = $props();
	import '../app.css';


	let notes = $state([])

	onMount(async ()=> {
		const res = await ftch('/notes')
		notes = JSON.parse(res)


		// register commands here 
		unregisterAll();
		await register('CommandOrControl+Shift+P', () => {
  		console.log('Shortcut triggered');
		});
		await register('CommandOrControl+Shift+O', () => {
  		console.log('Shortcut triggered');
		});
		await register('CommandOrControl+Shift+T', () => {
  		console.log('Shortcut triggered');
		});
		await register('CommandOrControl+Shift+C', () => {
  		console.log('Shortcut triggered');
		});
	})
</script>



<Terminal />



<div class="flex flex-row h-screen w-full">
	<Aside notes={notes} />
	<main class="p-2">
		{@render children()}
	</main>
</div>

