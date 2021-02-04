import React, {useState} from 'react';
import {useHistory} from 'react-router-dom';
import {Container, Divider, Segment, Header, Grid, Table} from 'semantic-ui-react';


const ProjectView = () => {
  const project_dummy = {
    id: 1,
    name: 'test',
    description: 'description',
  };

  const docker_dummy = {
    id: 1,
    name: 'asdf',
    image: 'ubuntu:latest',
    environments: {
      HOME: '/home/ubuntu/',
      PASSWORD: 'passw0rd',
    },
    ports: [
      {outer: 8080, inner: 80}
    ],
  };

  return (
    <Container>
      <Divider hidden/>
      <Segment raised>
        <Header as='h1'>{project_dummy.name}</Header>
        <Divider/>
        <Header as='h3'>Related docker</Header>
        <Table celled structured>
          <Table.Row>
            <Table.Cell>Container Name</Table.Cell>
            <Table.Cell>{docker_dummy.name}</Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell>Container Image</Table.Cell>
            <Table.Cell>{docker_dummy.image}</Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell>Environments</Table.Cell>
            <Table.Cell>
              {(docker_dummy.environments.length === 0) ? (
                <div>-</div>
              ) : (
                <>
                  hi
                </>
              )}
            </Table.Cell>
          </Table.Row>
        </Table>

      </Segment>
    </Container>
  );
};

export default ProjectView;
