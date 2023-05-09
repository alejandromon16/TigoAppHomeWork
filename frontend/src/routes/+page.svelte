<div>
    <div class="logo">
        <img src="logo.png" alt="">
    </div>

    
    <div class="loginForm">
        <h1>Login</h1>
        
        <form>
            <div>
                <label>Email:</label>
            </div>
                <input type="email"/>
            <div>
                <label>Password</label>
            </div>
            <input type="password"/>
            <div>
                <button type="submit">Login</button>
            </div>
        </form>
    </div>
</div>

<style>
    button{
        background-color: #00C8FF;
        padding: 15px 50px;
        width: 100%;
        border: none;
        border-radius: 20px;
        color: white;
        font-family: 'Roboto Medium', sans-serif;
    }

    input{
        outline: none;
        margin: 5px 10px;
        padding: 10px 20px;
        border: 1px solid;
        border-radius: 10px;
        border-color: #48c7f4;
    }

    h1{
        color: #00377d;
        font-family: 'Roboto Medium', sans-serif;
    }

    label{
        font-size: 20px;
        font-family: 'Roboto', sans-serif;
        color: #004d99;
    }

    form{
        display: flex;
        flex-direction: column;
        row-gap: 10px;
    }

    .loginForm{
        display: flex;
        width: max-content;
        flex-direction: column;
        justify-content: center;
        margin: auto;
        row-gap: 20px;
    }


    .logo{
        display: flex;
        justify-content: center;
        margin-top: 6rem;
    }

    img{
        width: auto;
        height: 140px;
    }
</style>