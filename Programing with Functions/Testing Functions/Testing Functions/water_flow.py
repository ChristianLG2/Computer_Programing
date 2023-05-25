
def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    density = 998.2
    gravity = 9.80665
    pressure = (density * gravity * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    density = 998.2
    pressure_loss = -(friction_factor * pipe_length * density * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    density_water = 998.2  # kg/m^3
    pressure_lossf = (-0.04 * density_water * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure_lossf

def reynolds_number(hydraulic_diameter, fluid_velocity):
    density_water = 998.2  # kg/m^3
    dynamic_viscosity_water = 0.0010016  # Pa*s
    reynolds = (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_water
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    density_water = 998.2  # kg/m^3
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    pressure_lossr = (-k * density_water * fluid_velocity**2) / 2000
    return pressure_lossr

def main():
    tower_height = float(input("Enter tower height: "))
    tank_height = float(input("Enter tank wall height: "))
    water_height = water_column_height(tower_height, tank_height)
    print(f"Water column height: {water_height} meters")

    pressure_gain = pressure_gain_from_water_height(water_height)
    print(f"Pressure gain: {pressure_gain} kilopascals")

    pipe_diameter = float(input("Enter pipe diameter: "))
    pipe_length = float(input("Enter pipe length: "))
    friction_factor = float(input("Enter friction factor: "))
    fluid_velocity = float(input("Enter fluid velocity: "))

    pressure_loss = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
    print(f"Pressure loss: {pressure_loss} kilopascals")

    quantity_fittings = int(input("Enter the quantity of fittings: "))
    pressure_lossf = pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
    print("Pressure loss due to fittings: {:.2f} kPa".format(pressure_lossf))

    hydraulic_diameter = float(input("Enter hydraulic diameter: "))
    reynolds = reynolds_number(hydraulic_diameter, fluid_velocity)
    print("Reynolds number: {:.2f}".format(reynolds))

    larger_diameter = float(input("Enter the larger diameter: "))
    smaller_diameter = float(input("Enter the smaller diameter: "))
    pressure_lossr = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds, smaller_diameter)
    print("Pressure loss due to pipe reduction: {:.2f} kPa".format(pressure_lossr))

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()









