<template>
	<div class="card flex justify-content-center">
			<AutoComplete v-model="value" :suggestions="items" @complete="search" />
	</div>
</template>

<script>
import AutoComplete from 'primevue/autocomplete';

export default {
	components: {AutoComplete},
	data() {
			return {
					value: '',
					items: []
			};
	},
	methods: {
			search(event) {
					this.items = [...Array(10).keys()].map((item) => event.query + '-' + item);
			}
	}
};
</script>