<!-- src/components/PlanCard.svelte -->
<script lang="ts">
    interface Plan {
        name: String;
        description: String;
        price: Number;
    }

    export let plan: Plan;

    let active: boolean = false;

    // Update the selected plan when the button is clicked
    function handleClick() {
        active = !active;
    }
</script>

<div class="card" class:active={active}>
    <h4>{plan.name}</h4>
    <h1>{plan.description}</h1>

    <div class="info">
        <button on:click class:active={active} on:click={handleClick}>
            {#if active}
                Seleccionado
            {:else}
                ME INTERESA
            {/if}
        </button>
        <div>
            <h1>Bs {plan.price}</h1>
        </div>
    </div>
</div>

<style>

    .info{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    /* Style the selected button */
    button.active {
        background-color: #98b2d4;
    }

    /* Add a border around the card if it is selected */
    .card.active {
        border: 2px solid #98b2d4;
    }

    /* Style the card */
    .card {
        padding: 20px 40px;
        background-color: #00377b;
        border-radius: 10px;
        cursor: pointer;
    }

    h1 {
        font-size: 20px;
        color: white;
        font-family: 'Roboto Medium', sans-serif;
    }

    h4 {
        font-size: 16px;
        color: white;
        font-family: 'Roboto Thin', sans-serif;
    }

    button {
        outline: none;
        background-color: #00C8FF;
        padding: 15px 50px;
        border: none;
        border-radius: 20px;
        color: white;
        font-family: 'Roboto Medium', sans-serif;
    }
</style>
