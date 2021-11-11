import ProjectCard from "../components/ProjectCard";
import useAuth from "../hooks/useAuth";
import styles from "../styles/Projects.module.css";

const Projects = () => {
	const { userId } = useAuth()

	// Fetch projects by USERID

	// Sample projects
	const projects = [
		{
			id: "1",
			name: "RTF",
			budget: 12000,
			description: "Realtime Face Recogniton"
		},
		{
			id: "2",
			name: "SWT",
			budget: 80000,
			description: "Smart Watch Tracker"
		},
		{
			id: "3",
			name: "ULS",
			budget: 11000,
			description: "Upgrade Legacy System"
		}
	]

	return (
		<div className={styles.outerContainer}>
			<div className={styles.projectsContainer}>
				<h1>Projects</h1>
				{projects.map((projectInfo) => {
					return (
						<ProjectCard projectInfo={projectInfo} />
					)
				})}
			</div>
		</div>
	)
}
export default Projects