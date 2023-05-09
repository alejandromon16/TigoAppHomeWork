<!-- src/routes/plans.svelte -->
<script lang="ts">
  import Logo from "../../components/Logo.svelte";
    import PlanCard from "../../components/PlanCard.svelte";
  import ServiceCard from "../../components/ServiceCard.svelte";

    interface Plan {
        name: String;
        description: String;
        price: number;
    }
    const plans:Plan[] = [
        { name: "PLAN TIGO HOGAR Inicial", description: "Hogar 20Mbps + TV", price: 199.0 },
        { name: "PLAN TIGO HOGAR Intermedio", description: "Hogar 40Mbps + TV + Movil ilimitado", price: 298.0 },
        { name: "PLAN TIGO HOGAR Avanzado", description: "Hogar 60Mbps + TV + Movil ilimitado + Netflix", price: 498.0 }
    ];

    const plansServices:Plan[] = [
        { name: "HBO", description:"", price:45},
        { name: "DISNEY", description:"", price:60},
        { name: "NETFLIX", description:"", price:35},

    ]

    let selectedPlans: Plan[] = [];

    // Update the selected plans
    function handleSelectPlan(plan:Plan) {
        let foundPlan = selectedPlans.find((p) => {
            if(p.name == plan.name){
                selectedPlans = selectedPlans.filter(p => p.name !== plan.name)
                return true;
            }
            return false;
        })

        if(!foundPlan){
            selectedPlans = [...selectedPlans, plan];
        }
    }

    $:{
        console.log(selectedPlans)
    }

    $: plansSelectedActive = selectedPlans.length > 0 ? true: false;
    $: totalPrice = selectedPlans.reduce((sum, plan) => sum + plan.price, 0);
</script>


<div class="main">

    <h1>Planes TIGO HOGAR</h1>
    
    {#each plans as plan}
        <div>.</div>
        <PlanCard plan={plan}  on:click={() => handleSelectPlan(plan)} />
    {/each}

    <h2>Servicios</h2>
    {#each plansServices as plan}
        <div>.</div>
        <ServiceCard plan={plan}  on:click={() => handleSelectPlan(plan)} />
    {/each}
    
    
    {#if plansSelectedActive}
        <h2>Planes Seleccionados:</h2>
        <ul>
            {#each selectedPlans as plan}
                <h5>{plan.name} Bs {plan.price}</h5>
            {/each}
        </ul>

        <h1>Total: <span>{totalPrice}</span></h1>
    {:else}
        <h2>No se ha seleccionado ningún plan</h2>
    {/if}


</div>

<style>

    h5{
        font-size: 16px;
        color: #5894e4;
        font-family: 'Roboto', sans-serif;   
    }
    .main{
        display: flex;
        flex-direction: column;
        padding-bottom: 20rem;
    }
    h1 {
        font-size: 32px;
        color: #00377d;
        font-family: 'Roboto Medium', sans-serif;
    }

    h2 {
        font-size: 24px;
        color: #00377d;
        font-family: 'Roboto Medium', sans-serif;
    }

</style>
