from abc import ABC
from typing import Optional, List


class VastAIBase(ABC):
    """VastAI SDK base class that defines the methods to be implemented by the VastAI class."""

    def attach_ssh(self, instance_id: int, ssh_key: str) -> str:
        """Attach an SSH key to an instance."""
        pass

    def cancel_copy(self, dst: str) -> str:
        """Cancel a file copy operation."""
        pass

    def cancel_sync(self, dst: str) -> str:
        """Cancel a file sync operation."""
        pass

    def change_bid(self, id: int, price: Optional[float] = None) -> str:
        """Change the bid price for a machine."""
        pass

    def copy(self, src: str, dst: str, identity: Optional[str] = None) -> str:
        """Copy files between instances."""
        pass

    def cloud_copy(
        self,
        src: Optional[str] = None,
        dst: Optional[str] = "/workspace",
        instance: Optional[str] = None,
        connection: Optional[str] = None,
        transfer: str = "Instance to Cloud",
    ) -> str:
        """Copy files between cloud and instance."""
        pass

    def create_api_key(
        self,
        name: Optional[str] = None,
        permission_file: Optional[str] = None,
        key_params: Optional[str] = None,
    ) -> str:
        """Create a new API key."""
        pass

    def create_ssh_key(self, ssh_key: str) -> str:
        """Create a new SSH key."""
        pass

    def create_workergroup(
        self,
        test_workers: int = 3,
        gpu_ram: Optional[float] = None,
        template_hash: Optional[str] = None,
        template_id: Optional[int] = None,
        search_params: Optional[str] = None,
        launch_args: Optional[str] = None,
        endpoint_name: Optional[str] = None,
        endpoint_id: Optional[int] = None,
        min_load: Optional[float] = None,
        target_util: Optional[float] = None,
        cold_mult: Optional[float] = None,
    ) -> str:
        """Create a new workergroup (autoscaler)."""
        pass

    # Backwards compatibility alias (deprecated: use create_workergroup)
    create_autogroup = create_workergroup

    def create_endpoint(
        self,
        min_load: float = 0.0,
        target_util: float = 0.9,
        cold_mult: float = 2.5,
        cold_workers: int = 5,
        max_workers: int = 20,
        endpoint_name: Optional[str] = None,
    ) -> str:
        """Create a new serverless endpoint."""
        pass

    def create_instance(
        self,
        id: int,
        price: Optional[float] = None,
        disk: Optional[float] = 10,
        image: Optional[str] = None,
        login: Optional[str] = None,
        label: Optional[str] = None,
        onstart: Optional[str] = None,
        onstart_cmd: Optional[str] = None,
        entrypoint: Optional[str] = None,
        ssh: bool = False,
        jupyter: bool = False,
        direct: bool = False,
        jupyter_dir: Optional[str] = None,
        jupyter_lab: bool = False,
        lang_utf8: bool = False,
        python_utf8: bool = False,
        extra: Optional[str] = None,
        env: Optional[str] = None,
        args: Optional[List[str]] = None,
        force: bool = False,
        cancel_unavail: bool = False,
        template_hash: Optional[str] = None,
    ) -> str:
        """Create a new instance from a contract offer ID."""
        pass

    def create_subaccount(
        self,
        email: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        type: Optional[str] = None,
    ) -> str:
        """Create a new subaccount."""
        pass

    def create_team(self, team_name: Optional[str] = None) -> str:
        """Create a new team."""
        pass

    def create_team_role(
        self, name: Optional[str] = None, permissions: Optional[str] = None
    ) -> str:
        """Create a new team role."""
        pass

    def create_template(
        self,
        name: Optional[str] = None,
        image: Optional[str] = None,
        image_tag: Optional[str] = None,
        login: Optional[str] = None,
        env: Optional[str] = None,
        ssh: bool = False,
        jupyter: bool = False,
        direct: bool = False,
        jupyter_dir: Optional[str] = None,
        jupyter_lab: bool = False,
        onstart_cmd: Optional[str] = None,
        search_params: Optional[str] = None,
        disk_space: Optional[str] = None,
    ) -> str:
        """Create a new template."""
        pass

    def delete_api_key(self, id: int) -> str:
        """Delete an API key."""
        pass

    def delete_ssh_key(self, id: int) -> str:
        """Delete an SSH key."""
        pass

    def delete_workergroup(self, id: int) -> str:
        """Delete a workergroup."""
        pass

    # Backwards compatibility alias (deprecated: use delete_workergroup)
    delete_autoscaler = delete_workergroup

    def delete_endpoint(self, id: int) -> str:
        """Delete a serverless endpoint."""
        pass

    def destroy_instance(self, id: int) -> str:
        """Destroy an instance."""
        pass

    def destroy_instances(self, ids: List[int]) -> str:
        """Destroy multiple instances."""
        pass

    def destroy_team(self) -> str:
        """Destroy the current team."""
        pass

    def detach_ssh(self, instance_id: int, ssh_key_id: str) -> str:
        """Detach an SSH key from an instance."""
        pass

    def execute(self, id: int, COMMAND: str) -> str:
        """Execute a command on an instance."""
        pass

    def invite_team_member(
        self, email: Optional[str] = None, role: Optional[str] = None
    ) -> str:
        """Invite a new member to the team."""
        pass

    def label_instance(self, id: int, label: str) -> str:
        """Label an instance."""
        pass

    def launch_instance(
        gpu_name: str,
        num_gpus: str,
        image: str,
        region: str = None,
        disk: float = 16.0,
        limit: int = 3,
        order: str = "score-",
        login: str = None,
        label: str = None,
        onstart: str = None,
        onstart_cmd: str = None,
        entrypoint: str = None,
        ssh: bool = False,
        jupyter: bool = False,
        direct: bool = False,
        jupyter_dir: str = None,
        jupyter_lab: bool = False,
        lang_utf8: bool = False,
        python_utf8: bool = False,
        extra: str = None,
        env: str = None,
        args: list = None,
        force: bool = False,
        cancel_unavail: bool = False,
        template_hash: str = None,
        explain: bool = False,
        raw: bool = False,
    ) -> str:
        """
        Launches the top instance from the search offers based on the given parameters.

        Returns:
            str: Confirmation message of the instance launch or details about the operation.
        """
        pass

    def logs(self, INSTANCE_ID: int, tail: Optional[str] = None) -> str:
        """Retrieve logs for an instance."""
        pass

    def prepay_instance(self, id: int, amount: float) -> str:
        """Prepay for an instance."""
        pass

    def reboot_instance(self, id: int) -> str:
        """Reboot an instance."""
        pass

    def recycle_instance(self, id: int) -> str:
        """Recycle an instance."""
        pass

    def remove_team_member(self, id: int) -> str:
        """Remove a member from the team."""
        pass

    def remove_team_role(self, NAME: str) -> str:
        """Remove a role from the team."""
        pass

    def reports(self, id: int) -> str:
        """Generate reports for a machine."""
        pass

    def reset_api_key(self) -> str:
        """Reset the API key."""
        pass

    def start_instance(self, id: int) -> str:
        """Start an instance."""
        pass

    def start_instances(self, ids: List[int]) -> str:
        """Start multiple instances."""
        pass

    def stop_instance(self, id: int) -> str:
        """Stop an instance."""
        pass

    def stop_instances(self, ids: List[int]) -> str:
        """Stop multiple instances."""
        pass

    def search_benchmarks(self, query: Optional[str] = None) -> str:
        """Search for benchmarks based on a query."""
        pass

    def search_invoices(self, query: Optional[str] = None) -> str:
        """Search for invoices based on a query."""
        pass

    def search_offers(
        self,
        type: Optional[str] = None,
        no_default: bool = False,
        new: bool = False,
        limit: Optional[int] = None,
        disable_bundling: bool = False,
        storage: Optional[float] = None,
        order: Optional[str] = None,
        query: Optional[str] = None,
    ) -> str:
        """Search for offers based on various criteria."""
        pass

    def search_templates(self, query: Optional[str] = None) -> str:
        """Search for templates based on a query."""
        pass

    def set_api_key(self, new_api_key: str) -> str:
        """Set a new API key."""
        pass

    def set_user(self, file: Optional[str] = None) -> str:
        """Set user parameters from a file."""
        pass

    def ssh_url(self, id: int) -> str:
        """Get the SSH URL for an instance."""
        pass

    def scp_url(self, id: int) -> str:
        """Get the SCP URL for transferring files to/from an instance."""
        pass

    def show_api_key(self, id: int) -> str:
        """Show details of an API key."""
        pass

    def show_api_keys(self) -> str:
        """Show all API keys."""
        pass

    def show_ssh_keys(self) -> str:
        """Show all SSH keys."""
        pass

    def show_workergroups(self) -> str:
        """Show all workergroups (autoscalers)."""
        pass

    # Backwards compatibility alias (deprecated: use show_workergroups)
    show_autoscalers = show_workergroups

    def show_endpoints(self) -> str:
        """Show all endpoints."""
        pass

    def show_connections(self) -> str:
        """Show all connections."""
        pass

    def show_deposit(self, Id: int) -> str:
        """Show deposit details for an instance."""
        pass

    def show_earnings(
        self,
        quiet: bool = False,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        machine_id: Optional[int] = None,
    ) -> str:
        """Show earnings information."""
        pass

    def show_invoices(
        self,
        quiet: bool = False,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        only_charges: bool = False,
        only_credits: bool = False,
        instance_label: Optional[str] = None,
    ) -> str:
        """Show invoice details."""
        pass

    def show_instance(self, id: int) -> str:
        """Show details of an instance."""
        pass

    def show_instances(self, quiet: bool = False) -> str:
        """Show all instances."""
        pass

    def show_ipaddrs(self) -> str:
        """Show IP addresses."""
        pass

    def show_user(self, quiet: bool = False) -> str:
        """Show user details."""
        pass

    def show_subaccounts(self, quiet: bool = False) -> str:
        """Show all subaccounts of the current user."""
        pass

    def show_team_members(self) -> str:
        """Show all team members."""
        pass

    def show_team_role(self, NAME: str) -> str:
        """Show details of a specific team role."""
        pass

    def show_team_roles(self) -> str:
        """Show all team roles."""
        pass

    def transfer_credit(self, recipient: str, amount: float) -> str:
        """Transfer credit to another account."""
        pass

    def update_workergroup(
        self,
        id: int,
        min_load: Optional[float] = None,
        target_util: Optional[float] = None,
        cold_mult: Optional[float] = None,
        test_workers: Optional[int] = None,
        gpu_ram: Optional[float] = None,
        template_hash: Optional[str] = None,
        template_id: Optional[int] = None,
        search_params: Optional[str] = None,
        launch_args: Optional[str] = None,
        endpoint_name: Optional[str] = None,
        endpoint_id: Optional[int] = None,
    ) -> str:
        """Update a workergroup (autoscaler)."""
        pass

    # Backwards compatibility alias (deprecated: use update_workergroup)
    update_autoscaler = update_workergroup

    def update_endpoint(
        self,
        id: int,
        min_load: Optional[float] = None,
        target_util: Optional[float] = None,
        cold_mult: Optional[float] = None,
        cold_workers: Optional[int] = None,
        max_workers: Optional[int] = None,
        endpoint_name: Optional[str] = None,
    ) -> str:
        """Update a serverless endpoint configuration."""
        pass

    def update_team_role(
        self, id: int, name: Optional[str] = None, permissions: Optional[str] = None
    ) -> str:
        """Update details of a team role."""
        pass

    def update_ssh_key(self, id: int, ssh_key: str) -> str:
        """Update an SSH key."""
        pass

    def generate_pdf_invoices(
        self,
        quiet: bool = False,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        only_charges: bool = False,
        only_credits: bool = False,
    ) -> str:
        """Generate PDF invoices based on filters."""
        pass

    def cleanup_machine(self, id: int) -> str:
        """Clean up a machine's configuration and resources."""
        pass

    def list_machine(
        self,
        id: int,
        price_gpu: Optional[float] = None,
        price_disk: Optional[float] = None,
        price_inetu: Optional[float] = None,
        price_inetd: Optional[float] = None,
        discount_rate: Optional[float] = None,
        min_chunk: Optional[int] = None,
        end_date: Optional[str] = None,
    ) -> str:
        """List details of a single machine with optional pricing and configuration parameters."""
        pass

    def list_machines(
        self,
        ids: List[int],
        price_gpu: Optional[float] = None,
        price_disk: Optional[float] = None,
        price_inetu: Optional[float] = None,
        price_inetd: Optional[float] = None,
        discount_rate: Optional[float] = None,
        min_chunk: Optional[int] = None,
        end_date: Optional[str] = None,
    ) -> str:
        """List details of multiple machines with optional pricing and configuration parameters."""
        pass

    def remove_defjob(self, id: int) -> str:
        """Remove the default job from a machine."""
        pass

    def set_defjob(
        self,
        id: int,
        price_gpu: Optional[float] = None,
        price_inetu: Optional[float] = None,
        price_inetd: Optional[float] = None,
        image: Optional[str] = None,
        args: Optional[List[str]] = None,
    ) -> str:
        """Set a default job on a machine with specified parameters."""
        pass

    def set_min_bid(self, id: int, price: Optional[float] = None) -> str:
        """Set the minimum bid price for a machine."""
        pass

    def schedule_maint(
        self, id: int, sdate: Optional[float] = None, duration: Optional[float] = None
    ) -> str:
        """Schedule maintenance for a machine."""
        pass

    def cancel_maint(self, id: int) -> str:
        """Cancel scheduled maintenance for a machine."""
        pass

    def unlist_machine(self, id: int) -> str:
        """Unlist a machine from being available for new jobs."""
        pass

    def show_machines(self, quiet: bool = False, filter: Optional[str] = None) -> str:
        """
        Retrieve and display a list of machines based on specified criteria.

        Parameters:
        - quiet (bool): If True, limit the output to minimal details such as IDs.
        - filter (str, optional): A string used to filter the machines based on specific criteria.

        Returns:
        - str: A string representation of the machines information, possibly formatted as JSON or a human-readable list.
        """
        pass

    # Volume Methods

    def clone_volume(
        self,
        source: int,
        dest: int,
        size: Optional[float] = None,
        disable_compression: bool = False,
    ) -> str:
        """Clone an existing volume to a new location.

        Args:
            source: ID of the volume contract being cloned.
            dest: ID of the volume offer the volume is being copied to.
            size: Size of the new volume contract in GB. Must be >= source and <= dest offer.
            disable_compression: If True, do not compress volume data before copying.

        Returns:
            Confirmation message or volume creation details.
        """
        pass

    def create_volume(
        self,
        id: int,
        size: float = 15,
        name: Optional[str] = None,
    ) -> str:
        """Create a new volume from an offer ID.

        Args:
            id: ID of the volume offer (from search volumes).
            size: Size in GB of the volume. Default is 15 GB.
            name: Optional name for the volume.

        Returns:
            Confirmation message with volume creation details.
        """
        pass

    def delete_volume(self, id: int) -> str:
        """Delete a volume.

        Args:
            id: ID of the volume contract to delete.

        Returns:
            Confirmation message of deletion.
        """
        pass

    def list_volume(
        self,
        id: int,
        price_disk: float = 0.10,
        size: int = 15,
        end_date: Optional[str] = None,
    ) -> str:
        """List disk space for rent as a volume on a machine.

        Args:
            id: ID of the machine to list volume on.
            price_disk: Storage price in $/GB/month. Default is $0.10/GB/month.
            size: Size of disk space allocated to offer in GB. Default is 15 GB.
            end_date: Contract offer expiration date (unix timestamp or MM/DD/YYYY format).

        Returns:
            Confirmation message with listing details.
        """
        pass

    def list_volumes(
        self,
        ids: List[int],
        price_disk: float = 0.10,
        size: int = 15,
        end_date: Optional[str] = None,
    ) -> str:
        """List disk space for rent as volumes on multiple machines.

        Args:
            ids: List of machine IDs to list volumes on.
            price_disk: Storage price in $/GB/month. Default is $0.10/GB/month.
            size: Size of disk space allocated to offer in GB. Default is 15 GB.
            end_date: Contract offer expiration date (unix timestamp or MM/DD/YYYY format).

        Returns:
            Confirmation message with listing details.
        """
        pass

    def search_volumes(
        self,
        query: Optional[str] = None,
        no_default: bool = False,
        limit: Optional[int] = None,
        storage: float = 1.0,
        order: str = "score-",
    ) -> str:
        """Search for volume offers using custom query.

        Args:
            query: Query string for filtering volumes.
            no_default: If True, disable default query filters.
            limit: Maximum number of results to return.
            storage: Amount of storage for pricing in GiB. Default is 1.0 GiB.
            order: Comma-separated list of fields to sort on. Default is 'score-'.

        Returns:
            List of matching volume offers.
        """
        pass

    def show_volumes(self, type: str = "all") -> str:
        """Show stats on owned volumes.

        Args:
            type: Volume type to display. Options: 'local', 'network', 'all'. Default is 'all'.

        Returns:
            List of owned volumes with their details.
        """
        pass

    def unlist_volume(self, id: int) -> str:
        """Unlist a volume offer.

        Args:
            id: Volume ID to unlist.

        Returns:
            Confirmation message of unlisting.
        """
        pass

    # Network Volume Methods

    def create_network_volume(
        self,
        id: int,
        size: float = 15,
        name: Optional[str] = None,
    ) -> str:
        """Create a new network volume from an offer ID.

        Args:
            id: ID of the network volume offer (from search network volumes).
            size: Size in GB of the network volume. Default is 15 GB.
            name: Optional name for the network volume.

        Returns:
            Confirmation message with network volume creation details.
        """
        pass

    def list_network_volume(
        self,
        disk_id: int,
        price_disk: float = 0.15,
        size: int = 15,
        end_date: Optional[str] = None,
    ) -> str:
        """List disk space for rent as a network volume.

        Args:
            disk_id: ID of the network disk to list.
            price_disk: Storage price in $/GB/month. Default is $0.15/GB/month.
            size: Size of disk space allocated to offer in GB. Default is 15 GB.
            end_date: Contract offer expiration date (unix timestamp or MM/DD/YYYY format).

        Returns:
            Confirmation message with listing details.
        """
        pass

    def search_network_volumes(
        self,
        query: Optional[str] = None,
        no_default: bool = False,
        limit: Optional[int] = None,
        storage: float = 1.0,
        order: str = "score-",
    ) -> str:
        """Search for network volume offers using custom query.

        Args:
            query: Query string for filtering network volumes.
            no_default: If True, disable default query filters.
            limit: Maximum number of results to return.
            storage: Amount of storage for pricing in GiB. Default is 1.0 GiB.
            order: Comma-separated list of fields to sort on. Default is 'score-'.

        Returns:
            List of matching network volume offers.
        """
        pass

    def unlist_network_volume(self, id: int) -> str:
        """Unlist a network volume offer.

        Args:
            id: Network volume offer ID to unlist.

        Returns:
            Confirmation message of unlisting.
        """
        pass

    # Cluster Methods

    def create_cluster(
        self,
        subnet: str,
        manager_id: int,
    ) -> str:
        """Create a new Vast cluster.

        Args:
            subnet: Local subnet for cluster (e.g., '0.0.0.0/24').
            manager_id: Machine ID of manager node in cluster. Must exist already.

        Returns:
            Confirmation message with cluster creation details.
        """
        pass

    def delete_cluster(self, cluster_id: int) -> str:
        """Delete a cluster.

        Args:
            cluster_id: ID of the cluster to delete.

        Returns:
            Confirmation message of deletion.
        """
        pass

    def join_cluster(
        self,
        cluster_id: int,
        machine_ids: List[int],
    ) -> str:
        """Join machines to a cluster.

        Args:
            cluster_id: ID of the cluster to add machines to.
            machine_ids: List of machine IDs to join to the cluster.

        Returns:
            Confirmation message of machines joining cluster.
        """
        pass

    def show_clusters(self) -> str:
        """Show clusters associated with your account.

        Returns:
            List of clusters with their details (id, subnet, node count, etc.).
        """
        pass

    # Overlay Methods

    def create_overlay(
        self,
        cluster_id: int,
        name: str,
    ) -> str:
        """Create an overlay network on top of a physical cluster.

        Args:
            cluster_id: ID of the cluster to create overlay on.
            name: Overlay network name.

        Returns:
            Confirmation message with overlay creation details.
        """
        pass

    def delete_overlay(self, overlay_identifier: str) -> str:
        """Delete an overlay network.

        Args:
            overlay_identifier: ID (int) or name (str) of the overlay to delete.

        Returns:
            Confirmation message of deletion.
        """
        pass

    def join_overlay(
        self,
        name: str,
        instance_id: int,
    ) -> str:
        """Add an instance to an overlay network.

        Args:
            name: Overlay network name to join instance to.
            instance_id: Instance ID to add to overlay.

        Returns:
            Confirmation message of instance joining overlay.
        """
        pass

    def show_overlays(self) -> str:
        """Show overlay networks associated with your account.

        Returns:
            List of overlays with their details (id, name, subnet, cluster_id, instances).
        """
        pass

    # Environment Variable Methods

    def create_env_var(
        self,
        name: str,
        value: str,
    ) -> str:
        """Create a new user environment variable.

        Args:
            name: Environment variable name.
            value: Environment variable value.

        Returns:
            Confirmation message with creation details.
        """
        pass

    def delete_env_var(self, name: str) -> str:
        """Delete an environment variable.

        Args:
            name: Name of the environment variable to delete.

        Returns:
            Confirmation message of deletion.
        """
        pass

    def update_env_var(
        self,
        name: str,
        value: str,
    ) -> str:
        """Update an existing environment variable.

        Args:
            name: Environment variable name to update.
            value: New value for the environment variable.

        Returns:
            Confirmation message with update details.
        """
        pass

    def show_env_vars(self, show_values: bool = False) -> str:
        """Show user environment variables.

        Args:
            show_values: If True, display actual values. Default is False (masked).

        Returns:
            List of environment variables (values masked unless show_values=True).
        """
        pass

    # Miscellaneous Methods

    def create_account(
        self,
        email: str,
        username: str,
        password: str,
    ) -> str:
        """Create a new account.

        Note: This command is deprecated. Use the web interface instead.

        Args:
            email: Email address for the new account.
            username: Username for the new account.
            password: Password for the new account.

        Returns:
            Deprecation message.
        """
        pass

    def add_network_disk(
        self,
        instance_id: int,
        volume_id: int,
        mount_path: str = "/mnt/network",
    ) -> str:
        """Add a network disk (volume) to an instance.

        Args:
            instance_id: ID of the instance to add the network disk to.
            volume_id: ID of the network volume to attach.
            mount_path: Path where the volume will be mounted. Default is '/mnt/network'.

        Returns:
            Confirmation message with attachment details.
        """
        pass

    # Machine Management Methods

    def defrag_machines(self, ids: List[int]) -> str:
        """Defragment machines to optimize GPU assignments.

        Rearranges GPU assignments to make more multi-GPU offers available.

        Args:
            ids: List of machine IDs to defragment.

        Returns:
            Defragment result message.
        """
        pass

    def delete_machine(self, id: int) -> str:
        """Delete a machine if not in use by clients.

        Force deletes a machine, disregarding host jobs on own machines.

        Args:
            id: ID of the machine to delete.

        Returns:
            Confirmation message of deletion.
        """
        pass

    def self_test_machine(
        self,
        machine_id: int,
        debugging: bool = False,
        ignore_requirements: bool = False,
    ) -> str:
        """Perform a self-test on a machine.

        Verifies machine compliance with required specifications and functionality.

        Args:
            machine_id: ID of the machine to test.
            debugging: Enable debugging output. Default is False.
            ignore_requirements: Ignore minimum system requirements. Default is False.

        Returns:
            Self-test results.
        """
        pass

    def show_machine(self, id: int, quiet: bool = False) -> str:
        """Show details of a single machine.

        Args:
            id: ID of the machine to display.
            quiet: If True, only display numeric IDs. Default is False.

        Returns:
            Machine details.
        """
        pass

    # Template Methods

    def delete_template(
        self,
        template_id: Optional[int] = None,
        hash_id: Optional[str] = None,
    ) -> str:
        """Delete a template by ID or hash.

        Note: Deleting a template only removes the user's relationship to a template.

        Args:
            template_id: Template ID to delete.
            hash_id: Hash ID of template to delete.

        Returns:
            Confirmation message.
        """
        pass

    def update_template(
        self,
        hash_id: str,
        name: Optional[str] = None,
        image: Optional[str] = None,
        image_tag: Optional[str] = None,
        login: Optional[str] = None,
        env: Optional[str] = None,
        ssh: bool = False,
        jupyter: bool = False,
        direct: bool = False,
        jupyter_dir: Optional[str] = None,
        jupyter_lab: bool = False,
        onstart_cmd: Optional[str] = None,
        search_params: Optional[str] = None,
        disk_space: Optional[str] = None,
        no_default: bool = False,
    ) -> str:
        """Update an existing template.

        Args:
            hash_id: Hash ID of the template to update.
            name: New name for the template.
            image: Docker image for the template.
            image_tag: Image tag.
            login: Docker login credentials.
            env: Environment variables string.
            ssh: Enable SSH access.
            jupyter: Enable Jupyter.
            direct: Enable direct port access.
            jupyter_dir: Jupyter working directory.
            jupyter_lab: Use JupyterLab instead of Jupyter Notebook.
            onstart_cmd: Command to run on startup.
            search_params: Search parameters for matching offers.
            disk_space: Recommended disk space.
            no_default: Disable default query filters.

        Returns:
            Update confirmation message.
        """
        pass

    # Snapshot Methods

    def take_snapshot(
        self,
        instance_id: int,
        repo: Optional[str] = None,
        container_registry: str = "docker.io",
        docker_login_user: Optional[str] = None,
        docker_login_pass: Optional[str] = None,
        pause: str = "true",
    ) -> str:
        """Take a container snapshot and push to registry.

        Args:
            instance_id: ID of the instance to snapshot.
            repo: Docker repository to push snapshot to.
            container_registry: Container registry URL. Default is 'docker.io'.
            docker_login_user: Registry username.
            docker_login_pass: Registry password or token.
            pause: Pause container during commit ('true'/'false'). Default is 'true'.

        Returns:
            Snapshot scheduling confirmation.
        """
        pass

    # Instance Update Methods

    def update_instance(
        self,
        id: int,
        template_id: Optional[int] = None,
        template_hash_id: Optional[str] = None,
        image: Optional[str] = None,
        args: Optional[str] = None,
        env: Optional[str] = None,
        onstart: Optional[str] = None,
    ) -> str:
        """Update instance configuration from a new/updated template.

        Args:
            id: ID of the instance to update.
            template_id: New template ID to associate.
            template_hash_id: New template hash ID to associate.
            image: New image UUID.
            args: New arguments for the instance.
            env: New environment variables.
            onstart: New onstart script.

        Returns:
            Update confirmation message.
        """
        pass

    # VM Copy Methods

    def vm_copy(self, src: int, dst: int) -> str:
        """Copy VM image from one instance to another.

        Note: Destination VM must be stopped during copy. Source VM does not need
        to be stopped, but it's recommended to stop it for the duration.

        Args:
            src: Instance ID of the source VM.
            dst: Instance ID of the destination VM.

        Returns:
            Copy operation confirmation.
        """
        pass

    # Team Member Methods

    def invite_member(
        self,
        email: str,
        role: Optional[str] = None,
    ) -> str:
        """Invite a member to the team.

        Args:
            email: Email address of the user to invite.
            role: Role to assign to the invited user.

        Returns:
            Invitation confirmation message.
        """
        pass

    def remove_member(self, id: int) -> str:
        """Remove a member from the team.

        Args:
            id: ID of the team member to remove.

        Returns:
            Removal confirmation message.
        """
        pass

    def show_members(self) -> str:
        """Show team members.

        Returns:
            List of team members.
        """
        pass

    # Log Methods

    def get_endpt_logs(
        self,
        id: int,
        level: int = 1,
        tail: Optional[int] = None,
    ) -> str:
        """Get logs for a serverless endpoint.

        Args:
            id: ID of the endpoint group to fetch logs from.
            level: Log detail level (0-3). Default is 1.
            tail: Number of log lines to return from the end.

        Returns:
            Endpoint logs.
        """
        pass

    def get_wrkgrp_logs(
        self,
        id: int,
        level: int = 1,
        tail: Optional[int] = None,
    ) -> str:
        """Get logs for a serverless worker group.

        Args:
            id: ID of the worker group to fetch logs from.
            level: Log detail level (0-3). Default is 1.
            tail: Number of log lines to return from the end.

        Returns:
            Worker group logs.
        """
        pass

    def show_audit_logs(self) -> str:
        """Show account audit logs.

        Displays history of important actions and IP address accesses.

        Returns:
            List of audit log entries.
        """
        pass

    # Scheduled Job Methods

    def delete_scheduled_job(self, id: int) -> str:
        """Delete a scheduled job.

        Args:
            id: ID of the scheduled job to delete.

        Returns:
            Deletion confirmation message.
        """
        pass

    def show_scheduled_jobs(self) -> str:
        """Show scheduled jobs.

        Returns:
            List of scheduled jobs for the account.
        """
        pass

    # Maintenance Methods

    def show_maints(self, ids: str, quiet: bool = False) -> str:
        """Show maintenance information for host machines.

        Args:
            ids: Comma-separated string of machine IDs.
            quiet: If True, only display numeric IDs. Default is False.

        Returns:
            Maintenance information for specified machines.
        """
        pass

    # Network Disk Methods

    def show_network_disks(self) -> str:
        """Show network disks associated with your account.

        Returns:
            Network disk information grouped by cluster.
        """
        pass

    # Invoice V1 Methods

    def show_invoices_v1(
        self,
        invoices: bool = False,
        charges: bool = False,
        invoice_type: Optional[List[str]] = None,
        charge_type: Optional[List[str]] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 20,
        next_token: Optional[str] = None,
        format: str = "table",
        verbose: bool = False,
        latest_first: bool = False,
    ) -> str:
        """Show invoices or charges with advanced filtering (v1 API).

        Args:
            invoices: Show invoices instead of charges.
            charges: Show charges instead of invoices.
            invoice_type: Filter by invoice types (transfers, stripe, bitpay, etc.).
            charge_type: Filter by charge types (instance, volume, serverless).
            start_date: Start date (YYYY-MM-DD or timestamp).
            end_date: End date (YYYY-MM-DD or timestamp).
            limit: Number of results per page (default: 20, max: 100).
            next_token: Pagination token for next page.
            format: Output format ('table' or 'tree'). Default is 'table'.
            verbose: Include full details (tree view only). Default is False.
            latest_first: Sort by latest first. Default is False.

        Returns:
            Invoice or charge information based on selected filters.
        """
        pass
