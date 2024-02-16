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
		<form v-on:submit.prevent="sendAffaire(e)">
			<label>Nom de l'affaire: </label>
			<input type="text" name="name" required v-model="name">

			<!-- Afficher un element form si unique -->
			<MultipleForm v-if="isActive === false" @child-event="handleChildEvent" />

			<!-- Boucler sur plusieurs formes si multiple -->
			<div v-if="isActive === true">
				<ul>
					<MultipleForm v-for="(formlieu, i) in lieu" :key="i" @child-event="handleChildEvent" />
				</ul>

				<!-- Ajouter un lieu -->
				<button @click="addLieu()">AJOUTER LIEU</button>

				<!-- Enlever un lieu -->
				<button v-if="lieuCount > 2" @click="removeLieu">ENLEVER LIEU</button>
			</div>

			<!-- VALIDATION DE L'AFFAIRE -->
			<button>VALIDER AFFAIRE</button>
		</form>
		<AffairesList />
	</div>
</template>


<script>
import AppTitle from './components/AppTitle.vue'
import MultipleForm from './components/MultipleForm.vue';
import AffairesList from './components/AffairesList.vue';

const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: this.name }, {infos: this.Infos})
	}

export default {
  name: 'App',
  components: {AppTitle, MultipleForm, AffairesList },

	data() {
		return {
			isActive: false,
			lieu: [MultipleForm, MultipleForm],
			lieuCount: 2,
			name: "",
			Infos: [
							{dpt: null, ville: null, prec: null}
						]
		};
	},
	methods: {
		/* Activer Unique ou Multiple */
			toggle() {
				this.isActive = this.isActive ? false : true;
			},

			/* Fonction pour ajouter un lieu */
			addLieu() {
				this.lieu.push(MultipleForm);
				this.lieuCount += 1;
			},

			/* Fonction pour enlever un lieu */
			removeLieu() {
				this.lieu.pop()
				this.lieuCount -= 1
			},

			/* Envoyer au back l'affaire */
			sendAffaire() {
				fetch('localhost:4000/create_case', requestOptions)
    		.then(response => response.json())
    		.then(data => product.value = data);
			},

			handleChildEvent(payload) {
				this.Infos.push(payload)
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