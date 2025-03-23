<script>
  let { notes } = $props()

</script>


<div class="flex flex-col gap-1 h-full w-[30%] border-r border-secondary p-2">
  <div class="flex flex-row gap-1">
    <button aria-label="addon" class="p-2 rounded-md border border-accent">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-terminal-plus" viewBox="0 0 16 16">
        <path d="M2 3a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h5.5a.5.5 0 0 1 0 1H2a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h11a2 2 0 0 1 2 2v4a.5.5 0 0 1-1 0V4a1 1 0 0 0-1-1z"/>
        <path d="M3.146 5.146a.5.5 0 0 1 .708 0L5.177 6.47a.75.75 0 0 1 0 1.06L3.854 8.854a.5.5 0 1 1-.708-.708L4.293 7 3.146 5.854a.5.5 0 0 1 0-.708M5.5 9a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1H6a.5.5 0 0 1-.5-.5M16 12.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0m-3.5-2a.5.5 0 0 0-.5.5v1h-1a.5.5 0 0 0 0 1h1v1a.5.5 0 0 0 1 0v-1h1a.5.5 0 0 0 0-1h-1v-1a.5.5 0 0 0-.5-.5"/>
      </svg>
    </button>
  </div>

  <h1>Notes</h1>

  <button class="text-left border border-accent p-2 rounded-md">
    {#each notes as note}
    <div class="flex flex-col">
      <p>{note.title}</p>
      <p class="text-neutral-300 text-xs">first works in this note</p>
    </div>
    {/each}
  </button>
</div>
