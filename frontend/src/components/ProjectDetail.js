import React from 'react';
import './ProjectDetail.css'
import { FiGrid } from "react-icons/fi";

function ProjectDetail({ project }) {
  return (
    <div className="custom-heading">
        <p className='p1'><b>{project.title}</b></p>
        <hr class="gray-line"></hr>
        <br></br>
        <p className='p2'><FiGrid /><b> Title</b></p>
        <p className='p3'>{project.title}</p>
        <br></br>

        <p className='p2'><FiGrid /><b> Project.Technologies</b></p>
        <p className='p3'>{project.technologies}</p>
        <br></br>

        <p className='p2'><FiGrid /><b> Technical_Skillset.Frontend</b></p>
        <p className='p3'>{project.technical_skillset.frontend}</p>
        <br></br>

        <p className='p2'><FiGrid /><b> Technical_Skillset.Backend</b></p>
        <p className='p3'>{project.technical_skillset.backend}</p>
        <br></br>

        <p className='p2'><FiGrid /><b> Technical_Skillset.Databases</b></p>
        <p className='p3'>{project.technical_skillset.databases}</p>
        <br></br>
        
        <p className='p2'><FiGrid /><b> Technical_Skillset.Infrastructure</b></p>
        <p className='p3'>{project.technical_skillset.infrastructure}</p>
    </div>
  );
}

export default ProjectDetail;
