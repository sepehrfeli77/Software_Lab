package com.unittest.codecoverage.samples;

import com.unittest.codecoverage.exceptions.PersonException;
import com.unittest.codecoverage.models.*;
import com.unittest.codecoverage.models.validators.PersonValidator;
import com.unittest.codecoverage.repositories.PersonRepository;
import com.unittest.codecoverage.services.impl.PersonServiceImpl;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.function.Executable;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.verify;

public class newTest {

    @Test
    public void getPersonNameTest() {
        Person person = new Person();
        person.setAge(21);
        person.setName("Sina Kazemi");
        person.setGender(Gender.M);

        assertEquals(21, person.getAge());
    }

    @Test
    public void requiredPersonNameTest() {
        Person person = new Person();
        person.setAge(21);
        person.setGender(Gender.F);

        PersonValidator personValidator = new PersonValidator();

        assertFalse(personValidator.requiredName(person.getName()));
    }

    @Test
    public void trafficGetStreetDirectionFlowTest() {
        Traffic traffic = new Traffic();
        traffic.setStreetDirectionFlow(StreetDirectionFlow.TWO_WAY);

        assertEquals(StreetDirectionFlow.TWO_WAY, traffic.getStreetDirectionFlow());
    }

    @Test
    public void trafficGetCurrentLightTest() {
        Traffic traffic = new Traffic();
        traffic.setCurrentTrafficLight(TrafficLigth.GREEN);

        assertEquals(TrafficLigth.GREEN, traffic.getCurrentTrafficLight());
    }

    @Test
    public void trafficGetMinSpeedAllowedTest() {
        Traffic traffic = new Traffic();
        traffic.setMinSpeedAllowed((short) 80);

        assertEquals((short) 80, traffic.getMinSpeedAllowed());
    }

    @Test
    public void trafficGetMaxSpeedAllowedTest() {
        Traffic traffic = new Traffic();
        traffic.setMaxSpeedAllowed((short) 100);

        assertEquals((short) 100, traffic.getMaxSpeedAllowed());
    }

    @Test
    public void footPassengerGetCrossedTheCrosswalkTest() {
        Footpassenger footpassenger = new Footpassenger();
        footpassenger.setCrossedTheCrosswalk(true);

        assertTrue(footpassenger.crossedTheCrosswalk());
    }

    @Test
    public void personRepositoryInsertPersonTest() {
        PersonRepository personRepository = new PersonRepository();

        assertThrows(NullPointerException.class, () -> personRepository.insert(null));
    }

    @Test
    public void deleteNameTest() {
        PersonServiceImpl personService = new PersonServiceImpl();

        assertThrows(PersonException.class, () -> personService.delete("Sina"));
    }


}
