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
    <button on:click class:active={active} on:click={handleClick}>
       {plan.name}
    </button>
<style>

    /* Style the selected button */
    button.active {
        background-color: #98b2d4;
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