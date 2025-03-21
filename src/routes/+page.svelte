<script lang="ts">
	import { GlobalState, preventDefault } from '$lib';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { marked } from 'marked';

	const gs = new GlobalState();

	$inspect(gs.greet, gs.name);
	let something = $state()
	function Convert() {
		console.log(something)
		something = marked.parse(something)
		close.log(something)
	}

	const onsubmit = preventDefault(() => gs.nlen && gs.submit());
	const onclick = () => gs.reset();
</script>

<h1 class="text-3xl font-bold">Name of note</h1>

<p contenteditable="true" bind:innerHTML={something}>
	#	notes in md format
	| Month    | Savings |
	| -------- | ------- |
	| January  | $250    |
	| February | $80     |
	| March    | $420    |

</p>

{@html something}

<button onclick={() => Convert()}>Convert</button>

<style>
	table {
		border-collapse: collapse;
	}
	th, td {
		border: 1px solid #000;
		padding: 5px;
	}
	</style>