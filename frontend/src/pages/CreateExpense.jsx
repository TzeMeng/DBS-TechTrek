import styles from "../styles/CreateExpense.module.css";

const CreateExpense = () => {
	return (
		<div className={styles.outerPage}>
			<h1>Create new expense</h1>
			<form className={styles.form}>
				<label>Name of expense</label>
				<input
					className={styles.input}
					type="text"
				/>
				<label>Description</label>
				<input
					className={styles.input}
					type="text"
				/>
				<label>Amount</label>
				<input
					type="number"
					className={styles.inputNumber}
				/>
				<input
					type="submit"
					className={styles.submitButton}
				/>
			</form>
		</div>
	)
}
export default CreateExpense