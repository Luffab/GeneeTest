<!-- Element unique d'un formulaire -->
<template>
	<form id ="Multiple" v-on:submit.prevent="saveForm">
		<div>
			<label>Departement: </label>
			<input type="text" required id = "dpt" v-model="tab.dpt">
			<label>Commune: </label>
			<input type="text" required v-model="tab.ville">
		</div>
		<div>
			<label>Precisions: </label>
			<input type="text" required v-model="tab.prec">
		</div>
		<div>
			<button>Valider</button>
		</div>
	</form>
</template>

<script>

export default{
	//components: {AutocompleteAffaire},
	data() {
		return {
			tab: [{
				dpt: null,
				ville: null,
				prec: null,
			}],
			value: '',
      items: []
		}
	},
	methods: {
		/* Envoyer le resultat du formulaire a App.vue */
		saveForm() {
			this.$emit("child-event", this.tab)
		},
		search(event) {
            this.items = [...Array(10).keys()].map((item) => event.query + '-' + item);
        }
	}
}
</script>

<!-- CSS d'un element de formulaire -->
<style>
	#Multiple{
		border-style: solid;
		margin-left: 300px;
		margin-right : 300px;
		margin-top: 25px;
		margin-bottom: 25px;
	}
	div{
		display: block;
		padding: 10px 6px;
		margin-left: auto;
		margin-right: auto;
	}
	#dpt {
		margin-right: 5px;
	}
</style>