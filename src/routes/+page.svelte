<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { Input } from '$lib/components/ui/input/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { marked } from 'marked';


	let something = $state()
	function Convert() {
		console.log(something)
		something = marked.parse(something)
		console.log(something)
	}

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


<button onclick={() => Convert()}>Convert</button>
