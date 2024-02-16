<!-- Element unique d'un formulaire -->

<template>
	<form id ="Multiple">
		<div>
			<label>Departement: </label>
			<input type="text" required id = "dpt">
			<label>Commune: </label>
			<input type="text" required>
		</div>
		<div>
			<label>Precisions: </label>
			<input type="text" required>
		</div>
	</form>
</template>

<script>
export default{
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