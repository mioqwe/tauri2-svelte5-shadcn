<script>
  let { openfunction, open = true } = $props()
  import * as Dialog from "$lib/components/ui/dialog";

  function OpenTerminal() {
    openfunction();
    open = true;
  }


</script>

<Dialog.Root bind:open>
  <Dialog.Content class="bg-primary text-white">
    <Dialog.Header>
      <Dialog.Title>Are you sure absolutely sure?</Dialog.Title>
      <Dialog.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </Dialog.Description>
    </Dialog.Header>
  </Dialog.Content>
</Dialog.Root>