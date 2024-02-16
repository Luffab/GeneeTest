<template>
	<div>
		<!-- Titre de l'appli -->
		<AppTitle />

		<!-- Bouton pour changer entre unique et multiple -->
		<button
			class="ui button big toggle"
			:class="{active:isActive}"
			@click="toggle"
			>{{isActive ? 'MULTIPLE' : 'UNIQUE'}}</button>

		<!-- Definir le nom de l'affaire -->
		<label>Nom de l'affaire: </label>
		<input type="text" required>

		<!-- Afficher un element form si unique -->
		<MultipleForm v-if="isActive === false"/>

		<!-- Boucler sur plusieurs formes si multiple -->
		<div v-if="isActive === true">
			<ul>
				<MultipleForm v-for="(formlieu, i) in lieu" :key="i" />
			</ul>

			<!-- Ajouter un lieu -->
			<button @click="addLieu()">AJOUTER LIEU</button>

			<!-- Enlever un lieu -->
			<button v-if="lieuCount > 2" @click="removeLieu">ENLEVER LIEU</button>
		</div>

		<!-- VALIDATION DE L'AFFAIRE -->
		<button>VALIDER AFFAIRE</button>
		<AffairesList />
	</div>
</template>

<script>
import AppTitle from './components/AppTitle.vue'
import MultipleForm from './components/MultipleForm.vue';
import AffairesList from './components/AffairesList.vue';

export default {
  name: 'App',
  components: {AppTitle, MultipleForm, AffairesList },

	data() {
		return {
			isActive: false,
			lieu: [MultipleForm, MultipleForm],
			lieuCount: 2
		};
	},
	methods: {
		/* Activer Unique ou Multiple */
			toggle() {
				this.isActive = this.isActive ? false : true;
			},

			/* Fonction pour ajouter un lieu */
			addLieu() {
				this.lieu.push({component: MultipleForm});
				this.lieuCount += 1;
			},

			/* Fonction pour enlever un lieu */
			removeLieu() {
				this.lieu.pop()
				this.lieuCount -= 1
			}
		}
}
</script>

<!--CSS de l'app-->
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
