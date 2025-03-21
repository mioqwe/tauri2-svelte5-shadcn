<script lang="ts">
	import Aside from '$lib/comps/aside.svelte';
import '../app.css';
	let { children } = $props();
</script>



<div class="flex flex-row h-screen w-full">
	<Aside />
	<main class="p-2">
		{@render children()}
	</main>
</div>

