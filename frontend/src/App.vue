<template>
	<div>
		<AppTitle />
		<button
			class="ui button big toggle"
			:class="{active:isActive}"
			@click="toggle"
			>{{isActive ? 'MULTIPLE' : 'UNIQUE'}}</button>
		<label>Nom de l'affaire: </label>
		<input type="text" required>
		<AffaireForm v-if="isActive === false"/>
		<div v-if="isActive === true">
			<ul>
				<MultipleForm v-for="(formlieu, i) in lieu" :key="i" />
			</ul>
			<button @click="addLieu">AJOUTER LIEU</button>
			<button @click="removeLieu">ENLEVER LIEU</button>
		</div>
		<button>VALIDER AFFAIRE</button>
		<AffairesList />
	</div>
</template>

<script>
import AffaireForm from './components/AffaireForm.vue'
import AppTitle from './components/AppTitle.vue'
import MultipleForm from './components/MultipleForm.vue';
import AffairesList from './components/AffairesList.vue';

export default {
  name: 'App',
  components: { AffaireForm, AppTitle, MultipleForm, AffairesList },

	data() {
		return {
			isActive: false,
			lieu: [MultipleForm, MultipleForm],
		};
	},
	methods: {
			toggle() {
				this.isActive = this.isActive ? false : true;
			},
			addLieu() {
				this.lieu.push(MultipleForm);
				this.lieuCount += 1;
			},
			removeLieu() {
				this.lieu.pop()
				this.lieuCount -= 1
			}
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
