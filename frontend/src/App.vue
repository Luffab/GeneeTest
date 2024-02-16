<template>
	<div>
		<AppTitle />
		<button
			class="ui button big toggle"
			:class="{active:isActive}"
			@click="toggle"
			>{{isActive ? 'MULTIPLE' : 'UNIQUE'}}</button>
		<AffaireForm />
	</div>
</template>

<script>
import AffaireForm from './components/AffaireForm.vue'
import AppTitle from './components/AppTitle.vue'

export default {
  name: 'App',
  components: { AffaireForm, AppTitle },

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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

button {
		display: block;
		padding: 10px 6px;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 15px;
	}
</style>
