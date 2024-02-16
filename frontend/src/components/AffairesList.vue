<template>
	<ul>
		<li v-for="(affaire, i) in affaires" :key="i">{{ affaire }}</li>
	</ul>
</template>

<script>
export default {
    data() {
			return {
				affaires: ['Affaire1', 'Affaire2']
			};
		},
	}
</script>