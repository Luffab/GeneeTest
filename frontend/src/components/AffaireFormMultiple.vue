<template>
	<form>
		<div>
			<label>Departement: </label>
			<input type="text" required id = "dpt">
			<label>Commune: </label>
			<input type="text" required>
		</div>
		<div>
			<label>Precisions: </label>
			<input type="text" required id = "dpt">
		</div>
		<button @click="removeLieu">ENLEVER LIEU</button>
		<button @click="addLieu">AJOUTER LIEU</button>
	</form>
</template>

<script>
export default{

}
</script>

<style>
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