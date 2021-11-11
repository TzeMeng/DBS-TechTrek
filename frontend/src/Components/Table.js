import styles from "../styles/Table.module.css";

const Table = ({ title, data }) => {
  const createTable = () => {
    const row = data.length;
    const col = Object.keys(data[0]).length;

    let table = [];

    const header_names = Object.keys(data[0]);

    // header
    let header = [];
    for (let k = 0; k < col; k++) {
		console.log(header_names[k])
      header.push(<th key={`header${k}`}>{header_names[k]}</th>);
    }
    table.push(<tr key="header">{header}</tr>);

    // rows
    for (let i = 0; i < row; i++) {
      let children = [];

      // columns
      for (let j = 0; j < col; j++) {
        children.push(<td key={j}>{data[0][header_names[j]]}</td>);
      }

      //Create the parent and add the children
      table.push(<tr key={i}>{children}</tr>);
    }
    return table;
  };

  return (
    <div>
      <h1>{title}</h1>

      <table className="">
        <tbody>{createTable(data)}</tbody>
      </table>
    </div>
  );
};

// default value in props
Table.defaultProps = {
  title: "Budget Management Application",
};

export default Table;
