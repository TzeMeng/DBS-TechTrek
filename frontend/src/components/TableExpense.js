import { Table } from "react-bootstrap";

const TableExpense = ({ title, data }) => {
  const row = data.length;
  const header_names = Object.keys(data[0]);

  var dataFiltered = [];

  for (let i = 0; i < row; i++) {
    let expense = data[i];
    dataFiltered.push({
      id: expense.id,
      name: expense.name,
      description: expense.description,
      amount: expense.amount,
    });
  }

  // console.log("filter", dataFiltered);

  const createTable = (data) => {
    // const routeChange = () => {
    //   href={`/projects/${projectInfo.id}`}
    // }


    // console.log(data);
    const row = data.length;
    const col = Object.keys(data[0]).length;

    let table = [];

    const header_names = Object.keys(data[0]);

    // header
    let header = [];
    for (let k = 0; k < col; k++) {
      if (header_names[k] != "id") {
        // console.log(header_names[k])
        header.push(<th key={`header${k}`}>{header_names[k]}</th>);
      }
    }
    table.push(<tr key="header">{header}</tr>);

    // rows
    for (let i = 0; i < row; i++) {
      let children = [];

      // columns
      for (let j = 0; j < col; j++) {
        if (header_names[j] != "id") {
          children.push(<td key={j}>{data[i][header_names[j]]}</td>);
        }
      }

      //Create the parent and add the children
      table.push(
        <tr key={data[i]['id']} onClick={() => {window.open(`/expenses/${data[i]['id']}`, "_self")}}>
          {children}
        </tr>
      );
    }
    return table;
  };

  return (
    <div>
      <Table>
        <tbody>{createTable(dataFiltered)}</tbody>
      </Table>
    </div>
  );
};

// default value in props
Table.defaultProps = {
  title: "Budget Management Application",
};

export default TableExpense;
