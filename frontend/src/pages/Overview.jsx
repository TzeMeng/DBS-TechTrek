import { useHistory, useParams } from "react-router";
import TableExpense from "../components/TableExpense";
import styles from "../styles/Overview.module.css";

const Overview = ({}) => {
	const { projectId } = useParams()
	const history = useHistory();

	const handleAddNewExpense = () => {
		history.push(`/projects/${projectId}/create`);
	}
	
	const expenses = [
		{
			"id": 1,
			"project_id": 2,
			"category_id": 2,
			"name": "Server Maintenance",
			"description": "Server maintenance and upgrading work to incorporate BC plans",
			"amount": 30000,
			"created_at": "2021-11-04T16:00:00.000Z",
			"created_by": "Jacky",
			"updated_at": "2021-11-06T16:00:00.000Z",
			"updated_by": "Jacky"
		},
		{
			"id": 2,
			"project_id": 3,
			"category_id": 4,
			"name": "Consultant",
			"description": "Consultancy services for integration work",
			"amount": 10000,
			"created_at": "2021-11-06T16:00:00.000Z",
			"created_by": "Helen",
			"updated_at": "2021-11-07T16:00:00.000Z",
			"updated_by": "Helen"
		}
	]

	const row = expenses.length;
    const header_names = Object.keys(expenses[0]);

	var dataFiltered = []

	for (let i = 0; i < row; i++) {
		let expense = expenses[i]
		dataFiltered.push({"name": expense.name, "description":expense.description, "amount":expense.amount})
	}

	return (
		<div className={styles.outerPage}>
			<h1>Overview of expenses</h1>
			<TableExpense data={dataFiltered}/>
			<button className={styles.button} onClick={handleAddNewExpense}>Add new expense</button>
		</div>
	)
}

export default Overview
