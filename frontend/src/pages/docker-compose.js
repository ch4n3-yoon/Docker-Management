import React from 'react';
import {Container, Divider, Segment, Header, Grid} from 'semantic-ui-react';

const DockerCompose = () => {
  const dummy_data = [
    {
      name: 'test project',
      description: 'for debug and test'
    },
    {
      name: 'test project 2',
      description: 'testtestsetset'
    }
  ]

  return (
    <Container>
      <Divider hidden/>
      <Segment raised>
        <Header as="h1">Your Docker Projects</Header>
        <Divider hidden />
        {(dummy_data.map((project) => (
          <Segment>
            <Grid celled="internally">
              <Grid.Row>
                <Grid.Column width={4}>
                  <Header>{project.name}</Header>
                </Grid.Column>
                <Grid.Column width={6}>
                  <div>{project.description}</div>
                </Grid.Column>
              </Grid.Row>
            </Grid>
          </Segment>
        )))}
      </Segment>
    </Container>
  )
}

export default DockerCompose;