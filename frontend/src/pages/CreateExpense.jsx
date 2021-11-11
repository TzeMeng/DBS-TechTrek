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
				<label>Category</label>
				<input
					className={styles.inputCategory}
					list="categories"
				/>
				<datalist id="categories">
					<option value="Production"></option>
					<option value="Operation" />
					<option value="Financial" />
					<option value="Vendor" />
					<option value="Manpower" />
					<option value="Software" />
					<option value="Hardware" />
				</datalist>
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