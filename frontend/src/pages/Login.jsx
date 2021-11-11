import { useState } from "react";
import { useHistory } from "react-router";
import useAuth from "../hooks/useAuth"
import { baseUrl } from "../lib/config";
import styles from "../styles/Login.module.css";

const Login = () => {
	const { isLoggedIn, setLogin } = useAuth();
	const [error, setError] = useState();
	const history = useHistory();

	const handleClick = async () => {
		const username = document.getElementById("username").value;
		const password = document.getElementById("password").value;
		if (!username || !password) {
			setError("Cannot leave fields blank")
			return;
		}
		const payload = {
			username: username,
			password: password,
		}
		console.log(payload);
		try {
			const res = await fetch(baseUrl + "/login", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(payload),
			})
			if (res.status == 401 || res.status == 404) {
				return;
			}
			const resData = await res.json();
			console.log(resData)
			setLogin(resData.access_token, resData.userId)
			history.push("/projects");
		} catch {
			setError("Bad username or password combination")
		}
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