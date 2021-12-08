<script>
	import '@styles/main.scss';
	import Sidemenu from '@components/SideMenu/SideMenu.svelte';

	
</script>
<aside>
	<Sidemenu />
</aside>

<main>
	<h1>Hello</h1>
	<slot />
</main>
<style>

	main {
		background-color: var(--yellow);
	}

</style>
