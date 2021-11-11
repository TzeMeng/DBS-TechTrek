import styles from "../styles/Projects.module.css";

const ProjectCard = ({ projectInfo }) => {
	return (
		<div className={styles.cardContainer}>
			<a className={styles.projectName} href={`/projects/${projectInfo.id}`}>{projectInfo.name}</a>
			<div className={styles.infoContainer}>
				<p>{projectInfo.description}</p>
				<p>Budget: ${projectInfo.budget}</p>
			</div>
		</div>
	);
}
export default ProjectCard