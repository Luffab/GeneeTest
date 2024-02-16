<template>
	<div>
		<button
			class="ui button big toggle"
			:class="{active:isActive}"
			@click="toggle"
			>{{isActive ? 'UNIQUE' : 'MULTIPLE'}}</button>
	</div>
</template>

<script>

export default {
    components: {
    },
    data() {
			return {
				isActive: false,
			};
		},
		methods: {
			toggle() {
				this.isActive = this.isActive ? false : true;
			},
		}
	}
</script>