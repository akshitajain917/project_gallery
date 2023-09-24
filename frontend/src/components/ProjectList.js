import React, { useState, useEffect } from 'react';
import { getProjectList } from './apiService'; // Import the API service
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import parse from "html-react-parser";
import ProjectDetail  from './ProjectDetail';
import './ProjectDetail.css'

function ProjectList() {
  const [projects, setProjects] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getProjectList();
        setProjects(data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  const handleCloseDetail = () => {
    setSelectedProject(null);
  };

  const handleProjectClick = (project) => {
    setSelectedProject(project);
  };

  return (
    <div>
    <h1 align="center">Project Details</h1>
    <hr></hr>
    {selectedProject && (
        <>
          <div className="overlay" onClick={handleCloseDetail}></div>
          <div className="project-detail-panel">
            <div className="project-detail-content">
              <ProjectDetail project={selectedProject} />
            </div>
          </div>
        </>
      )}
    <Container>
      <Row xs={2} md={4} className="g-4">
        {projects.map((output) => (
        <Col>
          <Card className='h-100' style={{ width: '130rem' }} key={output.id} onClick={() => handleProjectClick(output)} style={{ cursor: 'pointer' }} >
          <Card.Body>
              <Card.Subtitle className="mb-2 text-muted">Title</Card.Subtitle>
              <Card.Title>{parse(output.title)}</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Project.Technologies</Card.Subtitle>
              <Card.Title>{parse(output.technologies)}</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Technical_Skillset.Frontend</Card.Subtitle>
              <Card.Title>{parse(output.technical_skillset.frontend)}</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Technical_Skillset.Backend</Card.Subtitle>
              <Card.Title>{parse(output.technical_skillset.backend)}</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Technical_Skillset.Databases</Card.Subtitle>
              <Card.Title>{parse(output.technical_skillset.databases)}</Card.Title>
              <Card.Subtitle className="mb-2 text-muted">Technical_Skillset.Infrastructure</Card.Subtitle>
              <Card.Title>{parse(output.technical_skillset.infrastructure)}</Card.Title>
            </Card.Body>
          </Card>
        </Col>
        ))}
      </Row>
    </Container>
    </div>
  );
}

export default ProjectList;
