import { useState } from "react";
import { useHistory } from "react-router";
import useAuth from "../hooks/useAuth"
import styles from "../styles/Login.module.css";

const Login = () => {
	const { isLoggedIn, setLogin } = useAuth();
	const [error, setError] = useState();
	const history = useHistory();

	const handleClick = () => {
		const username = document.getElementById("username").value;
		const password = document.getElementById("password").value;
		if (!username || !password) {
			setError("Cannot leave fields blank")
			return;
		}
		// Fetch jwt here

		setLogin("accesstoken", "1");
		history.push("/projects");
	}

	return (
		<div className={styles.outerPage}>
			<div className={styles.loginContainer}>
				<p>Username</p>
				<input
					id="username"
					className={styles.input}
					type="text"
				/>
				<p>Password</p>
				<input
					id="password"
					className={styles.input}
					type="password"
				/>
				{error && 
					<p className={styles.errorMessage}>{error}</p>
				}
				<button onClick={handleClick} className={styles.button}>Login</button>
			</div>
		</div>
	)
}
export default Login