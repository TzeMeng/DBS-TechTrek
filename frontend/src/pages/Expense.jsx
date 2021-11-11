
const Expense = () => {

	// TODO: Query by expense
	
	// dummy data
	const expenseInfo = {
        id: 1,
        project_id: 2,
        category_id: 2,
        name: "Server Maintenance",
        description: "Server maintenance and upgrading work to incorporate BC plans",
        amount: 30000,
        created_at: "2021-11-04T16:00:00.000Z",
        created_by: "Jacky",
        updated_at: "2021-11-06T16:00:00.000Z",
        updated_by: "Jacky"
    }

	return (
		<div>
			This is the expense
		</div>
	)
}
export default Expense