<script>
    import { onMount } from 'svelte'; 
    import { api } from '$lib/api.js';

    let data = [];

    onMount(async() => {
        data = await api("/notes/4", { method: "GET" });
        console.log(data);
    });

</script>